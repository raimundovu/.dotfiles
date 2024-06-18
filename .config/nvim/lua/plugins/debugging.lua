return {
  "mfussenegger/nvim-dap",
  dependencies = {
    "rcarriga/nvim-dap-ui",
    "nvim-neotest/nvim-nio",
  },
  config = function()
    local dap = require("dap")
    local dapui = require("dapui")

    dapui.setup()

    dap.adapters.php = {
      type = "executable",
      command = "node",
      args = { os.getenv("HOME") .. "/vscode-php-debug/out/phpDebug.js" }
    }

    dap.configurations.php = {
      {
        type = "php",
        request = "launch",
        name = "Listen for Xdebug",
        port = 9000,
        log = true,
        pathMapping = {
          ["/application"] = "${workspaceFolder}"

        }
      }
    }

    dap.listeners.before.attach.dapui_config = function()
      dapui.open()
    end
    dap.listeners.before.launch.dapui_config = function()
      dapui.open()
    end
    dap.listeners.before.event_terminated.dapui_config = function()
      dapui.close()
    end
    dap.listeners.before.event_exited.dapui_config = function()
      dapui.close()
    end

    vim.keymap.set("n", "<Leader>dt", function()
      dap.toggle_breakpoint()
    end)

    vim.keymap.set("n", "<Leader>dc", function()
      dap.continue()
    end)

    vim.keymap.set("n", "<Leader>B", function()
      dap.set_breakpoint()
    end)
  end,
}
