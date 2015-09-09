class Trie
  def initialize
    @root = TrieNode.new(trie: self)
    @word_nodes = {}
    @concat_nodes = {}
    @both_nodes = []
  end

  def add_word(word)
    @root.add_word(word)
  end

  def add_concatenation(full_string)
    @root.add_concatenation(full_string)
  end

  def valid_word?(word)
    !!@word_nodes[word]
  end

  def valid_concatenation?(string)
    !!@concat_nodes[string]
  end

  def mark_concatenation(node)
    node.concat_present = true
    @concat_nodes[node.prefix] ||= node
  end

  def mark_word(node)
    node.word_present = true
    @word_nodes[node.prefix] ||= node
  end

  def import_words(word_list)
    word_list.each { |word| 
      add_word(word) 
    }
  end

  def find_concatenations
    @both_nodes = []
    words = @word_nodes.keys.sort {|x, y| x.length <=> y.length }
    queue = @word_nodes.to_a.sort {|x, y| y[0].length <=> x[0].length }
    until queue.empty?
      string, node = queue.shift
      #      puts string
      words.select {|word| word.length < string.length }.each do |word|
        chunk = string[-word.length..-1]
        if chunk == word
          if valid_word?(chunk)
            @both_nodes << node
          else
            queue << [string[0...-word.length], node]
          end
        end
      end
    end
    @both_nodes.sort! {|x, y| x.prefix.length <=> y.prefix.length }
  end

  def output_matches
    puts @both_nodes[-1]
    puts @both_nodes[-2]
    puts @both_nodes.length
  end
end

class TrieNode
  attr_accessor :word_present, :concat_present, :prefix, :children, :parent, :trie

  def initialize(options)
    @parent = options[:parent]
    @trie = options[:trie]
    @trie = @parent.trie if @parent
    @prefix = options[:prefix]
    @prefix ||= ""
    @word_present = options[:word_present]
    @word_present ||= false
    @concat_present = options[:concat_present]
    @concat_present ||= false
    @children = {}
  end

  def mark_word(word)
    @trie.mark_word(word)
  end

  def mark_concatenation(full_string)
    @trie.mark_concatenation(full_string)
  end

  def add_word(word)
    add_into_tree(word, true) { |node| mark_word(node) }
  end

  def add_concatenation(full_string)
    add_into_tree(full_string, false) { |node| mark_concatenation(node) }
  end

  def add_into_tree(string, extend_tree=true, &block)
    if string.length < prefix.length or string[0...prefix.length] != prefix
      throw "Bad Search Path, prefix #{prefix} and string #{string}"
    elsif string.length > prefix.length
      next_char = string[prefix.length]
      if children[next_char]
        #nothing
      elsif extend_tree
        children[next_char] = TrieNode.new(
          prefix: "#{prefix}#{next_char}", parent: self)
      else
        return nil
      end
      children[next_char].add_into_tree(string, &block)
    else #string and prefix are the same
      block.call(self)
      #return value is the node
    end
  end

  def find_parent(string)
    if string.length > prefix.length or string != prefix[-string.length..-1]
      throw "Bad Search Path, string #{string} is not a parent of #{prefix}"
    else
      node = self
      string.length.times { node = node.parent }
      return node
    end
  end


  def to_s
    "prefix, [#{children}]"
  end
end

File.open("wordsforproblem.txt") do |file|
  trie = Trie.new
  trie.import_words(file.lazy.map(&:strip))
  #trie.import_words(file.map(&:strip))
  #trie.generate_concatenations
  trie.find_concatenations
  trie.output_matches
end
