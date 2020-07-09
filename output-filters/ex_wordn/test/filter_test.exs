defmodule FilterTest do
  use ExUnit.Case
  doctest Filter

  test "should enumerate words" do
    assert Filter.enumerate("This is a test!", ~r{\s+}) == "[1]This [2]is [3]a [4]test!"
  end
end
