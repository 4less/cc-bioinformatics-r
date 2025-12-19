# Activate renv when available
if (file.exists("renv/activate.R")) {
  source("renv/activate.R")
  # Record all installed packages when snapshotting
  renv::settings$snapshot.type("explicit")
}
