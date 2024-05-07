#!/usr/bin/env ruby

pattern = /hb(?:t{2,5})n/

puts ARGV[0].scan(pattern).join
