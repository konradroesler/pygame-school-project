{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    python310
    git
  ];

  shellHook = ''
    if [ ! -d .venv ]; then
      python -m venv .venv
    fi

    source .venv/bin/activate
  '';
}
