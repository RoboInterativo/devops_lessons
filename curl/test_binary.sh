#!/usr/bin/expect
set token [lindex $argv 0]
set timeout 5

spawn telnet localhost 5000

expect "Connected"

send "GET /images/3301 HTTP/1.1\r"
send "Host: localhost\r\r"
expect "}"
