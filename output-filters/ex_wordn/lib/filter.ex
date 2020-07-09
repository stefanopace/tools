defmodule Filter do
  @moduledoc """
  Actual filters
  """

  @doc """
  Insert numbers before words

  ## Examples

      iex> Filter.enumerate("   ciccio benzina   ", " ")
      "[1]ciccio [2]benzina"

      iex> Filter.enumerate("Very\tnice      example!!!", ~r{[\s\t]+})
      "[1]Very [2]nice [3]example!!!"

      iex> Filter.enumerate("Super|Mario|Bros", "|")
      "[1]Super [2]Mario [3]Bros"

  """
  def enumerate(text, separator) do
    text
    |> tokenize(separator)
    |> add_numbers
    |> Enum.join(" ")
  end

  @doc """
  Only keep words with specified index

  ## Exapmles

    iex> Filter.keep("keep|this!", [2], "|")
    "this!"

    iex> Filter.keep("keep\tthis!", [2], ~r{[\s\t]+})
    "this!"

    iex> Filter.keep("keep this and that!", [2, 4], " ")
    "this that!"

  """
  def keep(text, indexes, separator) do
    text
    |> tokenize(separator)
    |> keep(indexes)
    |> Enum.join(" ")
  end

  def keep(list, indexes) do
    push_word_at = fn index, acc -> [word_at(list, index) | acc] end

    indexes
    |> Enum.reduce([], push_word_at)
    |> Enum.reverse()
  end


  @doc """
  Discard word at specified indexes

  ## Exapmles

    iex> Filter.discard("Discard this!", [2], " ")
    "Discard"

    iex> Filter.discard("dIsCaRd\tthis!", [2], ~r{[\s\t]+})
    "dIsCaRd"

    iex> Filter.discard("discard this and that!", [2, 4], " ")
    "discard and"

  """
  def discard(list, indexes) do
    discard(list, indexes, [], 1)
  end
  def discard([], _, acc, _) do
    acc
  end
  def discard([head | tail], indexes, acc, index) do
    to_delete = Enum.member?(indexes, index)
    if to_delete do
      discard(tail, indexes, acc, index + 1)
    else
      discard(tail, indexes, [head | acc], index + 1)
    end
  end
  def discard(text, indexes, separator) do
    text
    |> tokenize(separator)
    |> discard(indexes)
    |> Enum.reverse
    |> Enum.join(" ")
  end



  defp word_at(list, index) do
    {word, _} = List.pop_at(list, index - 1)
    word
  end

  defp tokenize(text, separator) do
    text
    |> String.trim()
    |> String.split(separator)
  end

  defp add_numbers(list), do: add_numbers(list, 1, [])
  defp add_numbers([], _, acc), do: Enum.reverse(acc)
  defp add_numbers(list, index, acc) do
    add_numbers(tl(list), index + 1, ["[#{index}]#{List.first(list)}" | acc])
  end
end
