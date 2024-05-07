#!/usr/bin/env ruby


pattern = /(h)(b*)(tn)$/

puts ARGV[0].scan(pattern).join
