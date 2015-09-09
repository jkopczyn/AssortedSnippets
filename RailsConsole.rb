class Post
  def initialize(options)
    @content = options[:content] || ""
  end

  def self.create(content)
    last = Post.new({content: content})
    @@db ||= [nil]
    @@db << last
    puts "Post created"
  end

  def self.find(idx)
    @@db[idx]
  end

  def self.last
    @@db[-1]
  end

  def to_s
    @content.to_s
  end

  def self.quit
  end
end


line = gets
while line != "quit"
  eval(line)
  line = gets
end
