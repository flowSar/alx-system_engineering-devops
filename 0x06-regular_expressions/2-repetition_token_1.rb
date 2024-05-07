#!/usr/bin/env ruby

arg=ARGV[0]

pattern = /((h)(b*)(tn))$/

if arg.nil?
    puts "enter argument"
    exit
end

result = arg.scan(pattern)

puts "#{result.join("")}"

