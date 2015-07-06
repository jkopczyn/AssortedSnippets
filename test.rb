# Parsing an API response
#
# Suppose you are calling a JSON API that responds to requests using a nested
# Hash, where the values are either other Hashes, or Strings, with no other
# possible options.
#
# Given a sequence of keys, write a method that traverses the Hash to return
# the String stored at the terminal key in the sequence.
def parse(hash, keys)
  dict = hash
  keys.each do |key|
    if dict.include?(key)
      dict = dict[key]
    else
      return nil
    end
  end
  if dict.is_a?(String)
    return dict
  else
    return nil
  end
end

input = {
  k1: "v1",
  k2: {
    k21: "v21",
    k22: {
      k221: "v221"
    }
  },
  k3: {
    k31: "v31"
  }
}


if (output = parse(input, [:k2, :k22, :k221]) == "v221")
  puts "Success!"
else
  puts "Output #{output.inspect} did not match 'v221'"
end
