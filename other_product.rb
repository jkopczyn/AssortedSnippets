input = []
product = 1
zeroes = 0
gets.to_i.times do
  input << gets.to_i
  if input.last == 0
    zeroes += 1
  else
    product *= input.last
  end
end
input.each do |n| 
  if zeroes == 0
    puts product/n
  elsif n == 0 and zeroes == 1
    puts product
  else
    puts 0
  end
end
