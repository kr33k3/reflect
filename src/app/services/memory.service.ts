import { Injectable } from '@angular/core';\
import { Storage } from '@ionic/storage';

@Injectable({
  providedIn: 'root'
})
export class MemoryService {

  constructor(private storage: Storage) { 
    this.storage.set('memories', this.generateMemories(3))
  }

  addMemories(memory: Memory) {
    this.getMemories().then(data => {
      data.push(memory)
      this.storage.set('memories', data)
    }).catch(err => {
      console.log('Error Add Memory')
      console.log(memory)
      console.log(err)
    })
  }

  getMemories(): Promise<any> {
    return this.storage.get('memories')
  }

  generateMemories(count: Number) {
    var memories = []
    for (var i = 0; i < count; i++) {
      memories.push(this.generateMemory())
    }
    return memories
  }

  generateMemory(): Memory {
    return {
      Title: "Bushido",
      Type: "Journal",
      ContentList: [{
        Title: 'Example One',
        Body: 'This is some common description or record',
        Attachments: [],
        Tags: []
      }],
      DateCreated: new Date()
    }
  }
}


interface Memory {
  Title: string;
  Type: string;
  ContentList: Content[];
  DateCreated: Date;
}

interface Content {
  Title: string;
  Body: string;
  Attachments: Attachment[];
  Tags: Link[];
}

interface Attachment {
  Base64: string;
  Title: string;
  Description: string;
  Tags: Link[];
}

interface Tag {
  Title: string;
  TagId: string;
}

interface Link {
  TagId: string;
  AssociatedGuid: string;
}

interface Reflection {
  Confidence: number;
  ReflectionDate: Date;
}
