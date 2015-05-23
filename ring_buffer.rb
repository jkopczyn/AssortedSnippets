class RingBuffer
  attr_reader :length, :start, :items, :arr

  def initialize(length)
    @length = length
    @arr = Array.new(10)
    @start = 0
    @items = 0
  end

  def append(*items)
    items.each do |item|
      self.push(item)
    end
  end

  def push(item)
    @arr[(@start+@items)% @length] = item
    if @items >= @length
      @start = (@start +1)% @length
    else
      @items += 1
    end
  end

  def remove(number)
    self.shift(number)
  end

  def shift(n=1)
    return nil if @items < n
    n.times { |i| @arr[@start+i] = nil }
    @start = (@start +n)% @length
    @items -= n
  end

  def list
    @items.times do |i|
      puts @arr[(@start+i)% @length]
    end
  end
end


size = gets.to_i
ring = RingBuffer.new(size)
while true
  command = gets.split
  if command[0] == "Q"
    break
  elsif command[0] == "L"
    ring.list
  elsif command[0] == "A"
    items = []
    command[1].to_i.times do
      items << gets
    end
    ring.append(*items)
  elsif command[0] == "R"
    ring.remove(command[1].to_i)
  else
    throw "Invalid Command"
  end
end
