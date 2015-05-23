class MaxHeap
  attr_reader :arr, :dict

  def initialize()
    @arr = []
    @dict = {}
  end

  def add(item)
    if @dict[item]
      @dict[item].val += 1
      heapify_up(@dict[item].index)
    else
      @arr << HeapNode.new(item, @arr, @arr.length)
      @dict[item] = @arr.last
      heapify_up
    end
  end

  def remove
    swap_nodes(@arr[0],arr[-1])
    ret = @arr.pop
    heapify_down
    return ret.key
  end

  def swap_nodes(a, b)
    throw "Heap Mismatch" unless a.heap == b.heap
    arr = a.heap
    arr[a.index], arr[b.index] = b, a
    a.index, b.index = b.index, a.index
    nil
  end

  def heapify_down
    return if @arr.empty?
    inspecting = @arr[0]
    while inspecting.left
      if inspecting < inspecting.left or (inspecting.right and 
            inspecting < inspecting.right)
        max_child = inspecting.right ? 
          [inspecting.left, inspecting.right].max : inspecting.left
        swap_nodes(inspecting, max_child)
      else
        break
      end
    end
    nil
  end

  def heapify_up(index=-1)
    inspecting = @arr[index]
    until inspecting.index == 0
      if inspecting > inspecting.parent
        swap_nodes(inspecting, inspecting.parent)
      else
        break
      end
    end
    nil
  end
end

class HeapNode
  include Comparable
  attr_accessor :val, :index
  attr_reader :key, :heap

  def initialize(key, heap, index)
    @key = key
    @val = 1
    @heap = heap
    @index = index
  end

  def parent
    @heap[(@index-1)/2]
  end

  def left
    @heap[1+(@index*2)] if 1+(@index*2) < @heap.length
  end

  def right
    @heap[(1+@index)*2] if (1+@index)*2 < @heap.length
  end

  def <=>(other)
    if val < other.val
      return -1
    elsif val > other.val
      return 1
    else
      return other.key <=> key
    end
  end
end

heap = MaxHeap.new
gets.to_i.times do
  heap.add(gets.chomp)
end
gets.to_i.times do
  puts heap.remove
end
