# cleandesktop

Moves documents on the `Desktop` directory into a folder called `Temp` hourly.

### Prerequisites

- A terminal
- crontab

### Installing

##### Configuring

Edit these lines of code in the `cleandesktop.py` file:

- `desktop_directory = "/Users/peterjmyers/Desktop"`
- `do_not_clean_files_and_folders = ['Documents', 'Temp', 'Inbox', 'Trash', '.DS_Store']`

##### Scheduling

1. Put the code below inside the file `~/.bash_profile`
2. Visit this project's directory and run `mk_cron_script`, and copy the result
3. Type `crontab -e` and paste that result on a new line (type :q and press enter to exit crontab)

		mk_cron_script() {
		  current_directory_py_file=""
		  venv_python_name=""

		  working_directory=`pwd`
		  for i in $working_directory/* ; do
		    extension=${i##*.}
		    if [[ $extension == "py" ]]; then
		      current_directory_py_file=$i
		    fi
		  done

		  for i in $working_directory/venv/bin/* ; do
		    path_before_period=$(echo $i | cut -d '.' -f 1)
		    file_before_period=${path_before_period##*/}
		    if [[ $file_before_period == "python2" || $file_before_period == "python3" ]]; then
		      venv_python_name=$i
		    fi
		  done

		  echo 0 \* \* \* \* $venv_python_name $current_directory_py_file
		}
