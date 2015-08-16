#
#"Anagram":  An anagram is a type of word play, the result of rearranging the 
#letters of a word or phrase to produce a new word or phrase using all the 
#original letters exactly once; for example, the letters from 'icon' can be rearranged into 'coin'.
#
#
#
#Devise a function that takes one parameter W and returns all the anagrams for W from the file wl.txt.
#
#
#anagrams("beat") should return:
#["beat", "beta", "bate"]
#
#
#
#=====================
#
#Test cases:
#
#anagrams("able") should return:
#['abel', 'able', 'bale', 'beal']
#
#anagrams("apple") should return:
#['appel', 'apple']
#
#anagrams("spot") should return:
#['post', 'pots', 'spot', 'stop', 'tops']
#
#anagrams("reset") should return:
#['reset', 'steer', "trees"]

def anagrams(word)
  dict_file = File.open("wl.txt")
  sorted_word = word.split("").sort.to_s
  results = []
  dict_file.each do |line|
    if line.chomp.split("").sort.to_s == sorted_word
      results << line.chomp
    end
  end
  dict_file.close
  results
end

def character_hash(word)
  hash = {}
  word.split("").each do |char|
    hash[char] ||= 0
    hash[char] += 1
  end
  hash
end

def anagrams2(word)
  dict_file = File.open("wl.txt")
  chosen_characters = character_hash(word)
  results = []
  dict_file.each do |line|
    results << line.chomp if character_hash(line.chomp) == chosen_characters
  end
  dict_file.close
  results
end
