#!/usr/bin/env ruby

pattern = /(?<=from:)(?:\w+)|(?<=to:)(?:\+?\d{11})|(?<=flags:)(?:-?\d:-?\d:-?\d:-?\d:-?\d)/
pattern2 = /:\w+/

argument = ARGV[0]

matches = argument.scan(pattern)
result = matches.join(",")
puts result
