#!/usr/bin/env ruby

pattern = /(?:from:\w+\S+)|(?:to:\+?\d{11})|(?:flags:-?\d:-?\d:-?\d:-?\d:-?\d)/

argument = ARGV[0]

matches = argument.scan(pattern)

puts "#{matches.join(", ")}"
