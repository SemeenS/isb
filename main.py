from work_with_txt_files import *
from work_with_json_files import *
from task2.bitwise_frequency import bitwise_frequency_test
from task2.identical_bit import identical_bit_test
from task2.longest_bit import longest_bit_test


def main():
    try:

        settings = read_json_file("settings.json")
        cpp_seq = open_txt_file(settings["cpp_seq"])
        java_seq = open_txt_file(settings["java_seq"])
        pi_values = settings["pi_values"]

        cpp_freq = bitwise_frequency_test(cpp_seq)
        cpp_identical = identical_bit_test(cpp_seq)
        cpp_longest = longest_bit_test(cpp_seq, pi_values)

        java_freq = bitwise_frequency_test(java_seq)
        java_identical = identical_bit_test(java_seq)
        java_longest = longest_bit_test(java_seq, pi_values)

        results = {
            "cpp": {
                "frequency_test": cpp_freq,
                "identical_bits_test": cpp_identical,
                "longest_run_test": cpp_longest,
            },
            "java": {
                "frequency_test": java_freq,
                "identical_bits_test": java_identical,
                "longest_run_test": java_longest,
            },
        }
        save_json_file(settings["result"], results)

    except Exception as e:
        print(f"Error:{e}")


if __name__ == "__main__":
    main()
