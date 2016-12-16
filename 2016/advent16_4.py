import string


class Security:
        def __init__(self):
                self.input_list = []
                self.sector_id_sum = 0
                self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                self.real_rooms = []
                self.decrypted_rooms = []
                                
        def readFile(self):
                input = open('input16_4.txt', 'r')
                for line in input:
                        word = ""
                        line = line.strip()
                        line = line.split('-')
                        for i in range(0, len(line)-1):
                                word += line[i]
                        [sector_id, checksum] = line[-1].split('[')
                        checksum = checksum.strip(']')
                        self.input_list.append((word, checksum, sector_id))
                input.close()

        def doStuff(self):
                self.readFile()
                for check_tuple in self.input_list:
                        encrypted_name, checksum, sector_id = check_tuple
                        encrypted_name = ''.join(sorted(encrypted_name))
                        partially_decrypted_name = self.check_counts(encrypted_name)
                        partially_decrypted_name = "".join(sorted(partially_decrypted_name))
                        checksum = "".join(sorted(checksum))
                        if partially_decrypted_name == checksum:
                                self.sector_id_sum += int(sector_id)
                                self.real_rooms.append(check_tuple)

                for room in self.real_rooms:
                        decrypted_name = ""
                        encrypted_name, checksum, sector_id = room
                        number_of_moves = int(sector_id)%26
                        for letter in encrypted_name:
                                start_index = self.alphabet.index(letter)
                                nytt_index = start_index + number_of_moves
                                if nytt_index > 25:
                                        nytt_index -= 26
                                decrypted_name += self.alphabet[nytt_index]
                        self.decrypted_rooms.append((decrypted_name, sector_id))

                for room in self.decrypted_rooms:
                        room_name, sector_id = room
                        if room_name.find('north')>-1:
                                print room_name, sector_id
                                

        def check_counts(self, check_string):
                top_five_letters = []
                all_letters = []
                return_item = ""
                for letter in self.alphabet:
                        count = check_string.count(letter)
                        all_letters.append((letter, count))
                sorted_list = sorted(all_letters, key=lambda x: x[1], reverse=True)
                top_five_letters = sorted_list[0:5]
                for item in top_five_letters:
                        return_item += item[0]
                return return_item
                
if __name__ == "__main__":
        x = Security()
        x.doStuff()
        print x.sector_id_sum
#        print x.decrypted_rooms
