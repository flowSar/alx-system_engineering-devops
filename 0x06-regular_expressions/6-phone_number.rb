#!/usr/bin/env ruby

pattern = /^[0-9]{10}/

puts ARGV[0].scan(pattern).join
