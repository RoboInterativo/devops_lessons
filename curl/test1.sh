#!/usr/bin/expect

set timeout 5

spawn telnet localhost 5000

expect "Connected"

send "GET / HTTP/1.1\r"
send "Host: localhost\r\r"
expect "</p>"
