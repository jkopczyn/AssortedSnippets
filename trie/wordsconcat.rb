require 'set'

class Trie
  attr_accessor :word_nodes, :root, :both_nodes

  def initialize
    @root = TrieNode.new(trie: self)
    @word_nodes = {}
    #@concat_nodes = {}
    @both_nodes = []
  end

  def add_word(word)
    @root.add_word(word)
  end

  def import_words(word_list)
    word_list.each { |word| add_word(word) }
    puts "words imported"
  end

  def valid_word?(string)
    !!@word_nodes[string]
  end

  def find_concat_words
    queue = @word_nodes.to_a.sort {|x, y| x[0].length <=> y[0].length }
    until queue.empty?
      prefix, node = queue.shift
      node.all_prefixes.map do |ancestor_node|
        rest = prefix[-ancestor_node.prefix.length..-1]
        if rest.empty? 
          next
        elsif valid_word?(rest)
          @both_nodes << node
          puts node.prefix
          break
        else
          queue << [rest, node]
        end
      end
    end
    @both_nodes.sort! {|x,y| x.prefix.length <=> y.prefix.length }
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

  def add_word(string)
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
      word_present = true
      @trie.word_nodes[prefix] = self
    end
  end

  def all_prefixes
    ancestors = Set.new()
    head = parent
    until head.parent.nil?
      ancestors << head if head.word_present
      head = head.parent
    end
    ancestors
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
