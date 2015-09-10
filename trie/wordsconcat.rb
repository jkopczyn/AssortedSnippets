require 'set'

class Trie
  attr_accessor :word_nodes, :root, :concatenated_words

  def initialize
    @root = TrieNode.new(trie: self, word_present: false)
    @word_nodes = {}
    @concatenated_words = Set.new
  end

  def add_word(word)
    @root.add_word(word)
  end

  def import_words(word_list)
    word_list.each { |word| add_word(word) unless word.empty? }
    puts "words imported"
  end

  def valid_word?(string)
    !!@word_nodes[string]
  end

  def find_concat_words
    queue = @word_nodes.to_a.sort {|x, y| x[0].length <=> y[0].length }
    until queue.empty?
      prefix, node = queue.shift
      ancestors_of(prefix, node, queue)
    end
  end

  def ancestors_of(string, node, queue)
    node.all_prefixes.map do |ancestor_node|
      rest = string[ancestor_node.prefix.length..-1]
      if rest.nil? or rest.empty? 
        next
      elsif valid_word?(rest)
        @concatenated_words << node.prefix
        return node.prefix
      else
        queue << [rest, node]
      end
    end
  end

  def output_matches
    largest = @concatenated_words.max_by {|x| x.length}
    puts largest
    puts (@concatenated_words - [largest]).max_by {|x| x.length}
    puts @concatenated_words.size
  end
end

class TrieNode
  attr_accessor :word_present, :prefix, :children, :parent, :trie

  def initialize(options)
    @parent = options[:parent]
    @trie = options[:trie]
    @trie = @parent.trie if @parent
    @prefix = options[:prefix]
    @prefix ||= ""
    @word_present = options[:word_present]
    @word_present ||= false
    @children = {}
  end

  def add_word(string)
    if string.length < prefix.length or string[0...prefix.length] != prefix
      throw "Bad Search Path, prefix #{prefix} and string #{string}"
    elsif string.length > prefix.length
      next_char = string[prefix.length]
      if !children[next_char]
        children[next_char] = TrieNode.new(
          prefix: "#{prefix}#{next_char}",
          parent: self, word_present: false)
      end
      children[next_char].add_word(string)
    else #string and prefix are the same
      @word_present = true
      @trie.word_nodes[prefix] = self
    end
  end

  def all_prefixes
    ancestors = []
    head = parent
    until head.nil?
      ancestors << head if head.word_present
      head = head.parent
    end
    ancestors
  end

  def to_s
    "#{prefix}, #{children.size} children"
  end
end

File.open("wordsforproblem.txt") do |file|
  trie = Trie.new
  trie.import_words(file.lazy.map(&:strip))
  trie.find_concat_words
  trie.output_matches
end
