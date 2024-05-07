#!/usr/bin/env ruby


pattern = /(h(?:b{,1})tn)/

puts ARGV[0].scan(pattern).join
