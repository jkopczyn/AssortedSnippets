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

  def generate_concatenations
    words = @word_nodes.keys.sort {|x, y| x.length <=> y.length }
    queue = words.dup
    until queue.empty?
      string = queue.shift
      puts string
      node = @word_nodes[string]
      words.each do |word|
        cand = "#{string}#{word}"
        if (!valid_concatenation?(cand)) and node.add_concatenation(cand)
          queue << cand
          @both_nodes << cand if valid_word?(cand)
        end
      end
    end
  end

  def output_matches
    puts @both_nodes[-1]
    puts @both_nodes[-2]
    puts @both_nodes.length
  end
end

class TrieNode
  attr_accessor :word_present, :concat_present, :prefix, :children

  def initialize(options)
    @trie = options[:trie]
    @prefix = options[:prefix]
    @prefix ||= ""
    @word_present = options[:word_present]
    @word_present ||= false
    @concat_present = options[:concat_present] or false
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
          prefix: "#{prefix}#{next_char}", trie: @trie)
      else
        return nil
      end
      children[next_char].add_into_tree(string, &block)
    else #string and prefix are the same
      block.call(self)
      #return value is the node
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
  trie.generate_concatenations
  trie.output_matches
end
