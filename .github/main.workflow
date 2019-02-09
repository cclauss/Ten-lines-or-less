workflow "New workflow" {
  on = "push"
  resolves = ["action"]
}

action "action" {
  uses = "cclauss/Find-Python-syntax-errors-action@master"
}
