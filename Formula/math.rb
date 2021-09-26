class Math < Formula
  desc "Command line math expression evaluator"
  homepage "https://docs.gridlabd.us/index.html?owner=dchassin&project=math&doc=/README.md"
  url "https://github.com/dchassin/math/raw/master/archive/v0.1.0.tar.gz"
  sha256 "84329cdb426d41c59a93ef53441a9541fd1a0d2ab00df0bc068ca273c33c6f88"
  license "BSD 3-Clause"

  def install
    system "make"
    system "make", "install", "PREFIX=#{prefix}"
  end

  test do
    system "#{bin}/math", "version"
  end
end
