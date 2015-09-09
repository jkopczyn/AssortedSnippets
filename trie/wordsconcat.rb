class Trie
end

class TrieNode
  attr_accessor :word_present, :concat_present, :prefix, :children

  def initialize(options)
    @prefix = options[:prefix] or ""
    @word_present = options[:word_present] or false
    @concat_present = options[:concat_present] or false
    @children = {}
  end

  def add_word(word)

  end

  def add_concatenation(full_string)

  end

  private
  def add_into_tree(string, &block)
    if string.length < @prefix.length or string[0...@prefix.length] != @prefix:
      throw "Bad Search Path, prefix #{@prefix} and string #{string}"
    elsif string.length > prefix.length:
      #add child if necessary and recurse
    end
  end
end
