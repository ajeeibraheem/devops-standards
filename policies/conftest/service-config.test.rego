package main

deny[msg] {
  not input.env.APP_ENV
  msg := "Missing APP_ENV in environment variables"
}

deny[msg] {
  input.resources.limits.cpu == ""
  msg := "CPU limit is not defined"
}

deny[msg] {
  input.resources.limits.memory == ""
  msg := "Memory limit is not defined"
}
