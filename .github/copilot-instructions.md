# Copilot Instructions for Gilded Rose Refactoring Kata

## Overview
This repository contains implementations of the Gilded Rose Refactoring Kata in multiple programming languages. The purpose of this file is to provide AI agents with guidance on how to assist developers working in this repository.

## Key Files and Directories
- **Main README**: [README.md](../README.md) provides an overview of the kata and links to requirements.
- **Language-specific directories**: Each subdirectory (e.g., `ruby/`, `zig/`, `lua/`) contains language-specific implementations and instructions.
- **Requirements**: The requirements for the kata are available in multiple languages (e.g., `GildedRoseRequirements.md`, `GildedRoseRequirements_zh.txt`).
- **Tests**: Most implementations include unit tests and/or text-based approval tests.

## Build and Test Commands
### General
- Refer to the `README.md` in each language-specific directory for detailed instructions.
- Common patterns include:
  - Running unit tests (e.g., `rspec` for Ruby, `zig build test` for Zig).
  - Running text-based approval tests (e.g., `ruby texttest_fixture.rb 10`).

### Examples
- **Ruby**:
  ```bash
  gem install rspec
  rspec gilded_rose_spec.rb
  ruby texttest_fixture.rb 10
  ```
- **Zig**:
  ```bash
  zig build test
  zig build
  ./zig/zig-out/bin/zig 10
  ```
- **Lua**:
  ```bash
  luarocks install --only-deps gildedrose-dev-1.rockspec
  busted
  lua src/main.lua 10
  ```

## Agent-Specific Instructions
### Refactoring Assistance
- Focus on small, incremental changes to improve code readability and maintainability.
- Ensure all tests pass after each change.

### Test Generation
- Use the requirements documents to identify edge cases and generate additional test cases.
- For text-based approval tests, ensure the output matches the expected results.

### Debugging
- When encountering issues, check the language-specific `README.md` for troubleshooting steps.
- Verify that all dependencies are installed and the environment is correctly configured.

## Potential Pitfalls
- Ensure compatibility with the specified versions of tools and dependencies (e.g., Ruby, Zig, Lua).
- Follow the conventions outlined in the language-specific `README.md` files.

## Example Prompts
- "Refactor the `update_quality` function in the Ruby implementation."
- "Add a new test case for the `Sulfuras` item in the Zig implementation."
- "Debug the failing test in the Lua implementation."

## Future Enhancements
- Add more detailed instructions for setting up and running tests in less-documented implementations.
- Standardize the structure and naming conventions across all language-specific directories.

## Python-specific instructions
- Focus only on the `python/` directory for this lab.
- Keep changes small and incremental.
- Preserve the public interface of `Item` and `GildedRose`.
- Prefer Strategy Pattern when refactoring item behavior.
- Run Python tests after each change.
- Add or update tests in `python/tests/test_gilded_rose.py`.