h = { AA: [[:AA]], BB: [[:BB]], CC: [[:CC]] }

# AA BB
# h[AA] = [innerA]
# h[BB] = [innerB]
# innerA = innerA + innerB
# h[BB] = [innerA]
{ AA: [[:AA, :BB]], BB: [[:AA, :BB]],  CC: [[:CC]] }
# CC BB
# h[CC] = [innerC]
# h[BB] = [innerA]
# innerA = innerC = innerC + innerA

def connected_components(edges)
  vertex_hash = {}
  edges.each do |pair|
    pair.each do |vertex|
      unless vertex_hash[vertex]
        vertex_hash[vertex] = [[vertex]]
      end
    end
    inner_left  = vertex_hash[pair[0][0]]
    inner_right = vertex_hash[pair[1][0]]
    inner_left = inner_right = (inner_left + inner_right)
  end
  component_set = Set.new
  vertex_hash.values.map do |value|
    component_set << Set.new(value[0]).to_a.map(:to_s)
  end
  component_set.to_a
end
