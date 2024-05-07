#!/usr/bin/env ruby

pattern = /(^h)(?:(.){1,1})(n$)/

puts ARGV[0].scan(pattern).join
