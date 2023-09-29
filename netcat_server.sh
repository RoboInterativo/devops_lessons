cat - > index.html <<<EOF
<!DOCTYPE html>
<html>
    <head>
        <title>Simple Netcat Server</title>
    </head>
    <body>
        <h1>Welcome to simple netcat server!<h1>
    </body>
    </body>
<html>
EOF

echo -e "HTTP/1.1 200 OK\n\n$(cat index.html)" | nc -l 1234
