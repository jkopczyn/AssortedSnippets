class Partial_Result
  attr_accessor :last_op, :last_number, :result, :child_results
  def initialize(options)
    @last_op = options[:last_op]
    @last_number = options[:last_number]
    @result = options[:result]
    @child_results = options[:child_results]
  end

  def [](operator)
    @child_results[operator.to_sym]
  end
end

def f(digit_string, target)
  digits = digit_string.split("").map(&:to_i)
  operators = ['+', '-', '*', '/', '']
  partial_results = {}
  #need to distinguish between operators and concats
  #partial results can be computed after operators but not after concats
  #possibly have entries be four parts: [last operator, last number, result,
  #hash of further results]

end

#a = Partial_Result.new({result: 1, last_number: 2, last_op: '+', child_results: {'a': 7}})
#puts a['a']
