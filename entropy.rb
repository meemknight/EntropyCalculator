require 'docx'


def readDOCX path
  doc = Docx::Document.open path

  doc.paragraphs.join "\n"
end

def remove_non_alpha text
  text.scan(/([a-zţşăîâșț]+)/).join " "
end

def compute_entropy word_list
  total = 0
  hash = {}

  word_list.each do |word|
    if hash[word]
      hash[word] = hash[word] + 1
      total += 1
    else 
      hash[word] = 1
      total += 1
    end
  end


  entropy = 0.0

  wordLength = hash.keys[0].length

  hash.each do |key, value|
    probab = (1.0 * value / total) / wordLength
    entropy += probab * Math.log(1/probab, 2)
  end
  
  entropy
end

def split_string_every_n_characters string, n

  string.scan(/.{#{n}}/)
end

p compute_entropy split_string_every_n_characters(remove_non_alpha(readDOCX "Ioan Slavici.docx"), 3)