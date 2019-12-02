  export interface Memory {
    Title: string;
    PageStart: number;
    PageEnd: number;
    Type: string;
    Tags: string[];
    ContentList: Content[];
    DateCreated: Date;
  }
  
  export interface Content {
    Title: string;
    Body: string;
    Attachments: Attachment[];
    Tags: string[];
  }
  
  export interface Attachment {
    Base64: string;
    Title: string;
    Description: string;
    Tags: Link[];
  }
  
  export interface Tag {
    Title: string;
    TagId: string;
  }
  
  export interface Link {
    TagId: string;
    AssociatedGuid: string;
  }
  
  export interface Reflection {
    Confidence: number;
    ReflectionDate: Date;
  }