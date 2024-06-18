return {
  "nvim-neotest/neotest",
  lazy = true,
  dependencies = {
    "nvim-neotest/nvim-nio",
    "antoinemadec/FixCursorHold.nvim",
    "olimorris/neotest-phpunit",
  },
  config = function()
    require("neotest").setup({
      adapters = {
        require("neotest-phpunit")({
          phpunit_cmd = function()
            return "vendor/bin/phpunit" -- for `dap` strategy then it must return string (table values will cause validation error)
          end,
          root_files = { "composer.json", "phpunit.xml", ".gitignore" },
          filter_dirs = { ".git", "node_modules" },
          env = {},  -- for example {XDEBUG_CONFIG = 'idekey=neotest'}
          dap = nil, -- to configure `dap` strategy put single element from `dap.configurations.php`
        }),
      }
    })
  end

}
