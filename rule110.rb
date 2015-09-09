def do_stuff(a, b)
  a = a.to_s
  b.downto(1) do |n|
    line = ("0"*n) + a
    puts line
    a = evolve_by_110(a)
  end
end

def evolve_by_110(string)
  storage = ""
  row = ["0","0"]+string.split("")+["0"]
  1.upto(row.length-2) do |n|
    storage << rule_110(row[n-1],row[n],row[n+1])
  end
  storage
end

def rule_110(l="0",c=nil,r="0")
  case "#{l}#{c}#{r}"
  when "110", "101", "011", "010", "001"
    return "1"
  else
    return "0"
  end
end


#boilerplate code
t = gets.to_i
for i in 1..t do
  a, b = gets.strip.split.map {|i| i.to_i}
  do_stuff(a, b)
end
