#!/usr/bin/env ruby

pattern = /hb(?:t*)n/

puts ARGV[0].scan(pattern).join
