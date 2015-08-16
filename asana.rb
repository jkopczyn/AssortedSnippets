def integer_division(product, divisor)
  quotient = 0
  factor = divisor
  power_of_2 = 0
  until factor >= product
    factor *= 2
    power_of_two += 1
  end
  until power_of_two < 0
    if factor <= product
      product -= factor
      quotient += pow2(power_of_two)
    end
    power_of_two -= 1
    factor = divisor*pow2(power_of_two)
  end
  [quotient, product] #remainder is now product
end

#helper
def pow2(exponent)
  i = 1
  exponent.downto(1) do
    i *= 2
  end
  i
end

class Tag
  def initialize(name, contents, options)
    @name = name
    @attributes = options
    @subelements = contents #array
  end

  def to_xml
    xml_string = "<#{@name}"
    @attributes.keys.each do |key|
      xml_string += " #{key}=\"#{@attributes[key]}\""
    end
    xml_string += ">"
    @subelements.each do |el|
      if el.is_a?(String)
        xml_string += el
      elsif el.is_a?(Tag)
        xml_string += el.to_xml
      else
        throw "Invalid subelement"
      end
    end
    xml_string += "</#{@name}>"
    return xml_string
  end
end

def order_dependencies(root, dependency_list)
  queue = Set.new(root)
  priority_hash = {root => 0}
  until queue.empty?
    file = queue.shift
    dependency_list[file].each do |dependency|
      unless priority_hash[dependency] and priority_hash[dependency] > priority_hash[file]
        priority_hash[dependency] = priority_hash[file]+1
        queue.push(dependency)
      end
    end
  end
  priority_hash.keys.sort {|key| priority_hash[key] }.reverse
end
