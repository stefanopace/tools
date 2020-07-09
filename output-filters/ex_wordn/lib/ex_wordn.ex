defmodule ExWordn do
  @moduledoc """
  Documentation for ExWordn.
  """

  def main(argv) do
    argv
    |> parse_args
    |> process

    System.halt(0)
  end

  @doc """
  Parse command arguments and return the subcommand to execute

  ## Examples

    iex> ExWordn.parse_args []
    %{command: :enumerate}

    iex> ExWordn.parse_args ["--separator", "#"]
    %{command: :enumerate, separator: "#"}

    iex> ExWordn.parse_args ["1", "4", "3"]
    %{command: :filter, keep: [1, 4, 3]}

    iex> ExWordn.parse_args ["1", "2", "3", "--separator", "|"]
    %{command: :filter, keep: [1, 2, 3], separator: "|"}

  """
  def parse_args(argv) do
    parse = OptionParser.parse(
      argv,
      strict: [
        delete: :boolean,
        separator: :string
      ],
      aliases: [
        d: :delete,
        s: :separator
      ]
    )

    case parse do
      {[separator: separator], [], _} ->
        %{
          command: :enumerate,
          separator: separator
        }

      {_, [], _} ->
        %{
          command: :enumerate
        }

      {[separator: separator], word_indexes, _} ->
        %{
          command: :filter,
          keep: to_integers(word_indexes),
          separator: separator
        }

      {[delete: true, separator: separator], word_indexes, _} ->
        %{
          command: :discard,
          discard: to_integers(word_indexes),
          separator: separator
        }

      {[separator: separator, delete: true], word_indexes, _} ->
        %{
          command: :discard,
          discard: to_integers(word_indexes),
          separator: separator
        }

      {[delete: true], word_indexes, _} ->
        %{
          command: :discard,
          discard: to_integers(word_indexes)
        }

      {_, word_indexes, _} ->
        %{
          command: :filter,
          keep: to_integers(word_indexes)
        }

    end
  end

  defp to_integers(string_numbers) do
    Enum.map(
      string_numbers,
      fn i ->
        {num, _} = Integer.parse(i)
        num
      end
    )
  end

  defp process(%{command: :discard, discard: indexes, separator: separator}) do
    fn text -> Filter.discard(text, indexes, separator) end
    |> for_each_line_form_stdin
  end

  defp process(%{command: :discard, discard: indexes}) do
    fn text -> Filter.discard(text, indexes, ~r{[\s\t]+}) end
    |> for_each_line_form_stdin
  end

  defp process(%{command: :enumerate, separator: separator}) do
    fn text -> Filter.enumerate(text, separator) end
    |> for_each_line_form_stdin
  end

  defp process(%{command: :enumerate}) do
    fn text -> Filter.enumerate(text, ~r{[\s\t]+}) end
    |> for_each_line_form_stdin
  end

  defp process(%{command: :filter, keep: indexes, separator: separator}) do
    fn text -> Filter.keep(text, indexes, separator) end
    |> for_each_line_form_stdin
  end

  defp process(%{command: :filter, keep: indexes}) do
    fn text -> Filter.keep(text, indexes, ~r{[\s\t]+}) end
    |> for_each_line_form_stdin
  end

  defp for_each_line_form_stdin(fun) do
    :stdio
    |> IO.read(:all)
    |> String.split("\n")
    |> remove_last_if_empty
    |> Enum.map(fun)
    |> Enum.each(fn text -> IO.puts(text) end)
  end

  defp remove_last_if_empty(lines) do
    lines
    |> Enum.reverse()
    |> remove_first_if_empty
    |> Enum.reverse()
  end

  defp remove_first_if_empty(["" | tail]), do: tail
  defp remove_first_if_empty(list), do: list
end
