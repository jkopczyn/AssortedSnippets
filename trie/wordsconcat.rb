class Trie
  def initialize
    @root = TrieNode.new
    @word_nodes = {}
    @concat_nodes = {}
  end

  def mark_concatenation(node)
    @concat_nodes[node.prefix] ||= node
    node.concat_present = true
  end

  def mark_word(node)
    @word_nodes[node.prefix] ||= node
    node.word_present = true
  end

  def valid_word?(word)
    !!@word_nodes[word]
  end

  def valid_concatenation?(string)
    !!@concat_nodes[string]
  end
end

class TrieNode
  attr_accessor :word_present, :concat_present, :prefix, :children

  def initialize(options)
    @trie = options[:trie]
    @prefix = options[:prefix] or ""
    @word_present = options[:word_present] or false
    @concat_present = options[:concat_present] or false
    @children = {}
  end

  def add_word(word)
    add_into_tree(full_string) { |node| node.trie.mark_word(node) }
  end

  def add_concatenation(full_string)
    add_into_tree(full_string) { |node| node.trie.mark_concatenation(node) }
  end

  def add_into_tree(string, &block)
    if string.length < prefix.length or string[0...prefix.length] != prefix:
      throw "Bad Search Path, prefix #{prefix} and string #{string}"
    elsif string.length > prefix.length:
      next_char = string[prefix.length]
      unless children[next_char]
        children[next_char] = TrieNode.new(
          prefix: "#{prefix}#{next_char}", trie: @trie)
      end
      children[next_char].add_into_tree(string, &block)
    else #string and prefix are the same
      block.call(self)
    end
  end

  def to_s
    "prefix, [#{children}]"
  end
end
