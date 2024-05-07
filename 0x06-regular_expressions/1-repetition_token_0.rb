#!/usr/bin/env ruby

arg=ARGV[0]

pattern = /^(hb)(t{2,})(n)$/

puts ARGV[0].scan(pattern).join


