from indeed import get_jobs
from save import save_to_file

indeed_jobs = get_jobs()

save_to_file(indeed_jobs)
