"""
For each repo in https://github.com/pulls, print any pull requests with git conflicts.
"""

import asyncio
from typing import AsyncGenerator

GET_PULLS = r"""gh search prs --author "$(gh api user --jq '.login')" --state open --limit=1000 --json repository,number,title --jq '.[] | "\(.repository.nameWithOwner)#\(.number): \(.title)"'"""
GET_PULL_REPOS = r"""gh search prs --author="$(gh api user --jq '.login')" --state=open --limit=1000 --json=repository --jq '.[] | .repository.nameWithOwner'"""
GET_CONFLICTING_PULLS = r"""gh pr list --repo {} --author="$(gh api user --jq '.login')" --json='number,mergeable' --jq '.[] | select(.mergeable == "CONFLICTING") | "\(.number)"'"""


async def my_run(command: str) -> AsyncGenerator[str, None]:
    process = await asyncio.create_subprocess_shell(
        command, shell=True, stdout=asyncio.subprocess.PIPE
    )
    async for line in process.stdout:
        yield line.decode("utf8").rstrip()
    await process.wait()


# async def get_pulls() -> AsyncGenerator[str, None]:
#    async for line in my_run(GET_PULLS):
#        yield line


async def get_pull_repos() -> list[str]:
    """Return a sorted list of repos with open pull requests.

    Use a set comprehension to remove duplicates.
    """
    return sorted({line async for line in my_run(GET_PULL_REPOS)})


async def get_conflicted_pulls() -> AsyncGenerator[str, None]:
    for i, repo in enumerate(await get_pull_repos(), 1):
        # if i % 10 == 0:
        #    print(f"Checking {i}th repo..")
        async for pull in my_run(GET_CONFLICTING_PULLS.format(repo)):
            yield f"https://github.com/{repo}/pull/{pull}/conflicts"


async def broken_get_conflicted_pulls() -> AsyncGenerator[str, None]:
    commands = [GET_CONFLICTING_PULLS.format(repo) for repo in await get_pull_repos()]
    async for result in asyncio.gather(*(my_run(command) for command in commands)):
        async for pull in result:
            yield pull


async def main():
    async for pull in get_conflicted_pulls():
        print(pull)
    # print("=" * 10)


if __name__ == "__main__":
    asyncio.run(main())
