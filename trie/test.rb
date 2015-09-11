File.open("wordsforproblem.txt", "r") do |file|
  File.open("tinywords.txt", "w") do |other|  
    file.each_with_index do |line, idx|    
      other.puts(line) if idx % 100 < 25 and (idx / 100) % 10 == 0      
    end  
  end  
end  
