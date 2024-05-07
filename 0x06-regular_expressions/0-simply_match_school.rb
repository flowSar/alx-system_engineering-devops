#!/usr/bin/env ruby

arg=ARGV[0]

pattern = /School/

result = arg.scan(pattern)

puts "#{result.join("")}"
