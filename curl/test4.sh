#!/usr/bin/expect
set token [lindex $argv 0]
set timeout 5

spawn telnet localhost 5000

#expect "Connected"
expect "'^]'."
send "POST /test_json HTTP/1.1\r"
send "Host: localhost\r"
send "Content-Type: application/json; charset=utf-8\r"
send "Accept-Ranges: bytes\r"
send "Content-Length: 46\r"
send "\r\r"
send '{"login":"my_login:,"password":"my_password"}'
send "\r\r"
expect eof
