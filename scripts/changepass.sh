#!/bin/bash
file=/root/.mysql_secret
var=$(cut -d: -f4- $file)
var="${var#"${var%%[![:space:]]*}"}"
mysqladmin -uroot -p$var password root
