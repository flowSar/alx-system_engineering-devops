#!/usr/bin/env ruby

pattern = /hb(?:t{,4})n/

puts ARGV[0].scan(pattern).join
