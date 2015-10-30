require 'byebug'

class Partial_Result
  attr_accessor :last_op, :last_number, :result, :child_results, :parent, :string_form
  def initialize(options)
    @last_op = options[:last_op].to_sym
    @last_number = options[:last_number]
    @result = options[:result]
    @child_results = {}
    @parent = options[:parent]
    @string_form = options[:string_form]
  end

  def [](operator)
    @child_results[operator.to_sym]
  end

  def []=(operator, value)
    @child_results[operator.to_sym] = value
  end
end


OPERATORS = ['+', '-', '*', '/', ''].map(&:to_sym)


def f(digit_string, target)
  digits = digit_string.split("").map(&:to_i)
  partial_results = Partial_Result.new(
    {result: 0, last_op: '+', last_number: digits[0], string_form: ""})
  #need to distinguish between operators and concats
  #partial results can be computed after operators but not after concats
  #possibly have entries be four parts: [last operator, last number, result,
  #hash of further results]
  solutions = []
  depth_first(digits, 0, target, partial_results, solutions)
  solutions.each { |soln| puts soln }
end

def depth_first(digits, depth, target, current_result, solutions)
  if depth < digits.length-1
    depth += 1
    OPERATORS.each do |op|
      if op == :''
        current_result[op] = Partial_Result.new({
          last_op: current_result.last_op, 
          last_number: 10*current_result.last_number+digits[depth],
          result: current_result.result,
          parent: current_result,
          string_form: current_result.string_form
        })
      else
        current_result[op] = Partial_Result.new({
          last_op: op,
          last_number: digits[depth],
          result: current_result.result.send(
            current_result.last_op, current_result.last_number),
          parent: current_result,
          string_form: "#{current_result.string_form} #{current_result.last_op} #{current_result.last_number}"
        })
      end
      depth_first(digits, depth, target, current_result[op], solutions)
    end
  else
    final= current_result.result.send(
      current_result.last_op, current_result.last_number)
    if final == target
      solutions << "#{current_result.string_form[3..-1]} #{current_result.last_op} #{current_result.last_number} = #{target}" 
      #debugger
    end
  end
  current_result
end
#a = Partial_Result.new({result: 1, last_number: 2, last_op: '+', child_results: {'a': 7}})
#puts a['a']

f("314", 16)
f("314", 15)
f("314", 14)
f("314", 13)
f("314", 12)
f("314", 11)
f("314", 10)
f("314", 9)
f("314", 8)
f("314159265358", 27182)
